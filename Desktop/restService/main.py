
from bottle import route, run, get, post, redirect, request
from bottle import template

@route('/index/<coordinate>')
def setCoordinate(coordinate):
        return template('This is the longitude {{longitude}}!', longitude=coordinate)

@route('/send')
def send():
        return '''
            <form action="/send" method="post">
                ID: <input name="cid" type="text"/>
                coordinate: <input name="cord" type="text" />
                <input value="send" type="submit"/>
            </form>
        '''
@route('/send', method='POST')
def do_send():

        global track_lists
        track_lists = dict()

        cid = request.forms.get('cid')
        cord = request.forms.get('cord')
        onelist = {cid : cord}

        if cid is not None and cord is not None:
                track_lists.update(onelist)

        redirect('/get')

@route('/get', method='GET')
@route('/get', method='POST')
def do_get():

        html = "<table border='1'>"
	html += "<tr><th>ID</th><th>Coordinate</th></tr>"
        for key in track_lists:
                html += "<tr><td> %s </td><td> %s </td> </tr></table>" % (key, track_lists[key])
		html += "<a href='/find'>search</a>"	
	
        return html

@route('/find')
def find():
	return template("form.tpl", message="find ID")


@route('/find', method ='POST')
def do_find():
	fcid = request.forms.get('fcid')

	
	if fcid is not None:
		if fcid in track_lists:
			html1 = "Record found!"
			html1 += "<table border='1'>"
			html1 += "<tr><th>ID</th><th>Coordinate</th></tr>"
			html1 += "<tr><td> %s </td><td> %s </td> </tr></table>" % (fcid, track_lists[fcid])
       			return html1
 
		else:
			html2 = "Not found. <a href ='/find'>search</a>"
			return html2	


run(host='localhost', port=8080, debug=True)
