from bottle import run,post,request,response,route
import os
import urllib

@post('/simple')
def simple_test():
    return "(:point_up: ՞ਊ ՞):point_up:"

if __name__ == '__main__':
    port_config = int(os.getenv('PORT', 5000))
    run(host='0.0.0.0', port=port_config)
