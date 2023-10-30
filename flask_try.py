from flask import Flask, request

# define the app
app = Flask(__name__)

# define the route, in this case '/' which is the root url, and the methods allowed (GET, POST)
# the function add() is called when the url is called
# get the arguments from the url using request.args.get("a"), this will expose model inputs to the url 
# and visible to the user or anyone who has access to the url
# post method is more secure, but it requires a form to be submitted, also if the function needs to handle 
# multiple arguments, it is better to use post method

# get method example
# @app.route('/', methods=['GET'])
# # create a function to add a and b
# def add():
    
#     # get the arguments from the url
#     a = request.args.get("a")
#     b = request.args.get("b")

#     # flask only return strings
#     return str(int(a)+int(b)) 

# post method example
@app.route('/', methods=['POST'])
# create a function to add a and b
def add():
    
    # get the arguments from a form submitted and raise error when the variable is missing in the post because of []
    # when the input is image or file, use post method
    a = request.form["a"]
    b = request.form["b"]

    # flask only return strings
    return str(int(a)+int(b)) 

# run the app
if __name__ == '__main__':
    app.run(port=7000) # run app on explicit port 7000

# run the app in terminal, and test in browser
# if using get method, the url will require the a and b arguments
# http://localhost:7000/?a=1&b=2
# if using post method, the url will not require the a and b arguments
# instead, need to use postman app's post request and "body" to provide a and b for http://localhost:7000/