from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:123@localhost/parasols'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer,primary_key=True)
    email_=db.Column(db.String(120),unique=True)
    fullName_=db.Column(db.String(50))
    address1_=db.Column(db.String(30))
    address2_=db.Column(db.String(30))
    city_=db.Column(db.String(30))
    stateAB_=db.Column(db.String(2))
    zipCode_=db.Column(db.Integer)
    phone_=db.Column(db.Integer)
    cardName_=db.Column(db.String(50))
    cardNo_=db.Column(db.Integer)
    expDate_=db.Column(db.Integer)
    cvvNo_=db.Column(db.Integer)
    product_=db.Column(db.String(50))
    price_=db.Column(db.Integer)

    def __init__(self, email_, fullName_, address1_, address2_, city_, stateAB_, zipCode_, phone_, cardName_, cardNo_, expDate_, cvvNo_, product_, price_):
        self.email_=email_
        self.fullName_=fullName_
        self.address1_=address1_
        self.address2_=address2_
        self.city_=city_
        self.stateAB_=stateAB_
        self.zipCode_=zipCode_
        self.phone_=phone_
        self.cardName_=cardName_
        self.cardNo_=cardNo_
        self.expDate_=expDate_
        self.cvvNo_=cvvNo_
        self.product_=product_
        self.price_=price_

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/thankyou", methods=['POST'])
def thankyou():
    if request.method=='POST':
        email=request.form["email_name"]
        fullName=request.form["fullName_name"]
        address1=request.form["address1_name"]
        address2=request.form["address2_name"]
        city=request.form["city_name"]
        stateAB=request.form["state_name"]
        zipCode=request.form["zipCode_name"]
        phone=request.form["phone_name"]
        cardName=request.form["cardName_name_name"]
        cardNo=request.form["cardNo_name_name"]
        expDate=request.form["expDate_name_name"]
        cvvNo=request.form["cvvNo_name_name"]
        product=request.form["product_name"]
        price=request.form["price_name"]
        
        print(request.form)
        
        data=Data(email, fullName, address1, address2, city, stateAB, zipCode, phone, cardName, cardNo, expDate, cvvNo, product, price)
        db.session.add(data)
        db.session.commit()
        return render_template("thankyou.html")

if __name__=='__main__':
    app.debug=True
    app.run()