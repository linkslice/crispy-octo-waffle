from flask import Blueprint, render_template, request, redirect, flash, current_app
import requests

teleport_bp = Blueprint('teleport', __name__)

@teleport_bp.route('/', methods=['GET', 'POST'])
def teleport_page():
    if request.method == 'POST':
        player = request.form['player']
        dimension = request.form['dimension']
        location = request.form['location']  # Update to use 'location' instead of 'coords'

        # Prepare parameters for the Jenkins job
        jenkins_url = f"{current_app.config['JENKINS_URL']}/job/{current_app.config['JENKINS_JOB_TELEPORT']}/buildWithParameters"
        auth = (current_app.config['JENKINS_USER'], current_app.config['JENKINS_TOKEN'])
        params = {
            "player": player,
            "dimension": dimension,
            "location": location  # Ensure the parameter matches the form field name
        }

        # Trigger Jenkins job
        response = requests.post(jenkins_url, auth=auth, data=params)

        if response.status_code == 201:
            flash("Teleportation request submitted successfully.", "success")
        else:
            flash(f"Error triggering teleportation job: {response.status_code}", "error")
        
        # Redirect back to the same page (or to another page if desired)
        return redirect(request.referrer or '/')

    return render_template('teleport.html')
