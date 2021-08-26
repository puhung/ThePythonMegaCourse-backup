import justpy as jp

def app():
    wp = jp.QuasarPage()
    #the first argument declares where h1 belongs.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews" )
    p1 = jp.QDiv(a=wp, text="These graph represent course review analysis")
    return wp

jp.justpy(app)