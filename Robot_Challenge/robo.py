from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='')

@app.route('/robot/')
@app.route('/robot/<id>')
@app.route('/robot/<id>/<param>')
def detail(id=None, name=None, param=1):

    the_name = None
    the_code = None

    if id == 'go':
        the_name = 'go'
        seconds = int(param)
        pause = seconds*1000

        return render_template('robot.html', id= id, seconds = seconds, pause = pause)
    elif id == 'square':
        the_name = 'square'
        seconds = int(param)
        pause = seconds*1000

        return render_template('robot.html', id= id, seconds = seconds, pause = pause)
    elif id == 'square':
        pause = int(param) * 2000
        the_name = 'Square Path Code'
        the_code = "\n"\
                +"symbol counter = b1\n"\
                +"    main:\n"\
                +"        ; Set Motor Speed Low\n"\
                +"        output C.5 \n"\
                +"        \n"\
                +"        doStuff:\n"\
                +"        for counter = 1 to 4\n"\
                +"            \n"\
                +"            gosub driveAndTurn\n"\
                +"            \n"\
                +"        next counter\n"\
                +"        \n"\
                +"        end\n"\
                +"\n"\
                +"    driveAndTurn:\n"\
                +"        ; Drive forward\n"\
                +"        forward A\n"\
                +"        forward B\n"\
                +"        pause "+str(pause)+"\n"\
                +"        \n"\
                +"        ; Turn right\n"\
                +"        halt A\n"\
                +"        halt B\n"\
                +"        forward A\n"\
                +"        pause 1000\n"\
                +"        halt A\n"\
                +"\n"\
                +"        return"

    elif id == '3':
        pause = int(param) * 2000
        the_name = 'Hexagon Path Code'
        the_code = "\n"\
                +"symbol counter = b1\n"\
                +"    main:\n"\
                +"        ; Set Motor Speed Low\n"\
                +"        output C.5 \n"\
                +"        \n"\
                +"        doStuff:\n"\
                +"        for counter = 1 to 6\n"\
                +"            \n"\
                +"            gosub driveAndTurn\n"\
                +"            \n"\
                +"        next counter\n"\
                +"        \n"\
                +"        end\n"\
                +"\n"\
                +"    driveAndTurn:\n"\
                +"        ; Drive forward\n"\
                +"        forward A\n"\
                +"        forward B\n"\
                +"        pause "+str(pause)+"\n"\
                +"        \n"\
                +"        ; Turn right\n"\
                +"        halt A\n"\
                +"        halt B\n"\
                +"        forward A\n"\
                +"        pause 750\n"\
                +"        halt A\n"\
                +"\n"\
                +"        return"


    return render_template('robot.html', name=the_name, code=the_code)

if __name__ == '__main__':
    app.run(debug=True)