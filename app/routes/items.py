from flask import Blueprint, render_template, request, redirect, current_app, flash
import requests

items_bp = Blueprint('items', __name__)

@items_bp.route('/', methods=['GET', 'POST'])
def manage_items():
    if request.method == 'POST':
        player = request.form['player']
        item = request.form['item']
        quantity = request.form['quantity']

        jenkins_url = f"{current_app.config['JENKINS_URL']}/job/{current_app.config['JENKINS_JOB_ITEMS']}/buildWithParameters"
        auth = (current_app.config['JENKINS_USER'], current_app.config['JENKINS_TOKEN'])
        params = {"player": player, "item": item, "quantity": quantity}

        try:
            response = requests.post(jenkins_url, auth=auth, data=params)
            response.raise_for_status()

            if response.status_code == 201:
                flash('Item successfully given!', 'success')
                return redirect('/')
            else:
                flash(f'Error triggering Jenkins job: {response.status_code}', 'error')
                return redirect('/')
        except requests.exceptions.RequestException as e:
            flash(f'Error triggering Jenkins job: {e}', 'error')
            return redirect('/')

    return render_template('items.html')
