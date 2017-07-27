import os
import uuid
import time
from flask import Flask

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#777799"
GREEN = "#99CC99"
COLOR = GREEN

with open("sessions2.txt") as f:
    mylist = f.read().splitlines()
f.close()
    
@app.route('/')
def mainmenu():
    response = """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">SE Conference<br/>
    {}</br>
    <a href="/agenda">Agenda</a><br>
    <a href="/floorplan">Floor plan</a>

    </center>
    </body>
    </html>
    """.format(COLOR,my_uuid,)
    return response


@app.route('/agenda')
def agenda():
    start_page = """<html><head></head><head>"""
    mid_page = """<h2>Agenda</h2>"""
    session_info = []
    
    for each_session in mylist:
        session_info = each_session.split(';')
        mid_page += """<a href="/agenda_detail/""" + session_info[0] + """">""" + session_info[1] + """</a><br>"""

    end_page = "</body></html>"
    full_page = start_page + mid_page + end_page
    
    return full_page

@app.route('/agenda_detail/<int:session_id>')
def agenda_detail(session_id):
       
    session_info = []
    session = mylist[session_id - 1]
    session_info = session.split(';')
    response = """   
    Topic : {}<br>
    Time: {}<br>
    Presenter: {}<br>
    <br>
    {}<br>

    """.format(session_info[1], time.ctime(float(session_info[2])), session_info[3],session_info[4])
    return response

@app.route('/floorplan')
def floorplan():
    response = """
    <html>
    <body bgcolor="{}">
    {}</br>
    <img src="/static/floorplan.jpg" alt="Floorplan">
    </body>
    </html>
    """.format(COLOR,my_uuid,)
    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
