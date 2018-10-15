from flask import Flask

app = Flask(__name__)
app.secret_key = '\/Y/-\$!$/-\|>!(|<'
app.static_folder = 'static'
'''

For the multitenant to work, and enabling subdomain detection, one needs to add URL rule. 
Without server name, flask cannot detect subdomains in localhost. When putting this into production
Comment out this part. 

Go to /etc/hosts and add a rule. 

127.0.0.1 local.com
'''
app.config['SERVER_NAME'] = 'local.com:5000'
@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=5000, debug=True)