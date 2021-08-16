
    //Array
  let shoppingCart = [];

//Shopping Cart
function displayShoppingCart(){
  let orderedProductsTblBody=document.getElementById("orderedProductsTblBody");

  while(orderedProductsTblBody.rows.length>0) {
      orderedProductsTblBody.deleteRow(0);
  }

  //Price of shopping cart
  let cart_total_price=0;
  
  
  for(let product in shoppingCart){

      let row=orderedProductsTblBody.insertRow();
      
      let cellName = row.insertCell(0);
      let cellDescription = row.insertCell(1);
      let cellPrice = row.insertCell(2);
      cellPrice.align="right";
      
      cellName.innerHTML = shoppingCart[product].Name;
      cellDescription.innerHTML = shoppingCart[product].Description;
      cellPrice.innerHTML = shoppingCart[product].Price;
      cart_total_price+=shoppingCart[product].Price;
  }

  //Total cost of products 
  document.getElementById("cart_total").innerHTML=cart_total_price;
  
}
  
//Add shipping

let shipping = document.getElementById('total_cost');

function applyShipping(shipping) {
  if (cart_total_price > 25.00)
  shipping = cart_total_price * 10 / 100;

  document.getElementById("total_cost").innerHTML=shipping;
  }
 
  

//--------------------------
function AddtoCart(name,description,price){

 let singleProduct = {};

 singleProduct.Name=name;
 singleProduct.Description=description;
 singleProduct.Price=price;

 shoppingCart.push(singleProduct);
 
 displayShoppingCart();

}
