from flask import Flask, render_template, session
from flask import request

import User
import Property
import Produce
import Visits
import FarmGrows

from flaskr import app

@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.route('/')
def index():
	if 'user' not in session.keys():
		return render_template('Login.html')
	elif session['user']['userType'] == 'admin':
		return render_template('HomescreenAdmin.html')
	elif session['user']['userType'] == 'owner':
		return render_template('HomescreenOwner.html')
	elif session['user']['userType'] == 'visitor':
		return render_template('HomescreenVisitor.html')
	else:
		return "Invalid Credentials"

@app.route('/register/owner')
def register_owner():
	return render_template('OwnerRegistration.html')

@app.route('/register/visitor')
def register_visitor():
	return render_template('VisitorRegistration.html')

@app.route('/Owner/OtherOwnerProperties')
def nav_to_other_owner_properties():
	return render_template('OtherOwnerPropertiesScreen.html')

@app.route('/')
def nav_to_homescreen_owner():
	return render_template('HomescreenOwner.html')

@app.route('/AddProperty')
def nav_to_add_property():
	return render_template('AddProperty.html')

@app.route('/ManageProperty')
def nav_to_manage_property():
	return render_template('ManageProperty.html')

@app.route('/ViewVisitorsListScreen')
def nav_to_view_visitors_list_screen():
    return render_template('ViewVisitorsListScreen.html')

@app.route('/ViewOwnersListScreen')
def nav_to_view_owners_list_screen():
    return render_template('ViewOwnersListScreen.html')

@app.route('/ConfirmedPropertiesAdminScreen.html')
def navToConfirmedPropertiesAdminScreen():
    return render_template('ConfirmedPropertiesAdminScreen.html')

@app.route('/UnconfirmedPropertiesAdminScreen')
def navToUnconfirmedPropertiesAdminScreen():
    return render_template('UnconfirmedPropertiesAdminScreen.html')

@app.route('/ApprovedAnimalsCropsScreen')
def navToApprovedAnimalsCropsScreen():
    return render_template('ApprovedAnimalsCropsScreen.html')

@app.route('/PendingAnimalsCropsScreen')
def navToPendingAnimalsCropsScreen():
    return render_template('PendingAnimalsCropsScreen.html')

@app.route('/HomescreenAdmin')
def navToHomescreenAdmin():
    return render_template('HomescreenAdmin.html')

if __name__ == '__main__':
	app.run()
