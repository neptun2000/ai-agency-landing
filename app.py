import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager
from models import Contact, Admin

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "a secret key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.form
        new_contact = Contact()
        new_contact.name = data['name']
        new_contact.email = data['email']
        new_contact.message = data['message']
        new_contact.submitted_at = datetime.utcnow()
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Admin.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        flash('Invalid username or password')
    
    return render_template('admin/login.html')

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    messages = Contact.query.order_by(Contact.submitted_at.desc()).all()
    return render_template('admin/dashboard.html', messages=messages)

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

def create_admin(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if not admin:
        admin = Admin()
        admin.username = username
        admin.password_hash = generate_password_hash(password)
        db.session.add(admin)
        db.session.commit()

with app.app_context():
    db.drop_all()  # Drop all existing tables
    db.create_all()  # Create tables with updated schema
    create_admin('admin', 'admin123')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
