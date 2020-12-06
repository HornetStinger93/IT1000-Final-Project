# IT1000-Final-Project
Final Project for IT1000
> By: _Jackson Samson_
### What is this?
![hmm](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/57173beb-3f7b-4eb7-b981-b806b692c025/dbi8k7k-819ed291-f68b-4642-81c6-84edea7f921a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNTcxNzNiZWItM2Y3Yi00ZWI3LWI5ODEtYjgwNmI2OTJjMDI1XC9kYmk4azdrLTgxOWVkMjkxLWY2OGItNDY0Mi04MWM2LTg0ZWRlYTdmOTIxYS5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.LagLhsEpNkAEByuW0a86GfpkRG02USQAcPsftExDDhw)
> That is a good question! This is my _markdown_ site for my final project in IT1000!   
I plan on taking you through five aspects of my life. 
* [Faith](/Faith.md)
* [Politics](/Politics.md)
* [Music](Music.md)
* [Careers](Careers.md)
* [Supertramp](Supertramp.md)
> These sites will be summaries of the topic and its relation to my life. Expect to see links to relevant music on every page (_except for careers, that one may be a bit boring_). 

Here is a **_meme_** I found on my computer (sorry for the [ifunny](https://www.ifunny.com/) watermark). ![picture](/7d3010413a3bb83817d1483715378a4ce4873ea6c5bb0d0ec7a2a164e456940d_1.jpg)

[YouTube](https://www.youtube.com/)

### Because you asked...
  Here is another block of code:
  ```
  <!DOCTYPE html>
<html>
<head>
   <!--
      JavaScript 6th Edition
      Chapter 7
      Hands-on Project 7-3

      Author:
      Date:

      Filename: index.htm
   -->
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
   <title>Hands-on Project 7-3</title>
   <link rel="stylesheet" href="styles.css" />
   <script src="modernizr.custom.05819.js"></script>
</head>

<body>
   <header>
      <h1>
      Restaurant Orders
      </h1>
   </header>

   <article>
      <h2>Lunch selections</h2>
      <form>
         <input type="checkbox" id="item1" value="799" />
         <label for="item1">Fried chicken ($7.99)</label>
         <input type="checkbox" id="item2" value="999" />
         <label for="item2">Fried halibut ($9.99)</label>
         <input type="checkbox" id="item3" value="799" />
         <label for="item3">Hamburger ($7.99)</label>
         <input type="checkbox" id="item4" value="1299" />
         <label for="item4">Grilled salmon ($12.99)</label>
         <input type="checkbox" id="item5" value="599" />
         <label for="item5">Side salad ($5.99)</label>
         <input type="button" value="Calculate" id="sButton" />
      </form>
      <table>
         <colgroup>
            <col class="label" />
            <col class="amount" />
         </colgroup>
         <tbody>
            <tr>
               <td>Item total</td>
               <td>0.00</td>
            </tr>
            <tr>
               <td>Tax</td>
               <td>0.00</td>
            </tr>
            <tr>
               <td>Total with tax</td>
               <td>$0.00</td>
            </tr>
         </tbody>
      </table>
   </article>
   <script>
      // function to add values of selected check boxes and display total
      function calcTotal() {
         var itemTotal = 0;
         var tax = 0;
         var totalWithTax = 0;
         var items = document.getElementsByTagName("input");
         var cells = document.getElementsByTagName("td");
         for (var i = 0; i < 5; i++) {
            if (items[i].checked) {
               itemTotal += (items[i].value * 1);
            }
         }
              if (itemTotal > 40) { itemTotal = itemTotal * .85 ;}
              else if (itemTotal > 30) {itemTotal = itemTotal * .90 ;}
              else if (itemTotal > 20) { itemTotal = itemTotal * .95;}



         
         tax = itemTotal * 0.05;
         totalWithTax = itemTotal + tax;
         cells[1].innerHTML = (itemTotal / 100).toFixed(2);
         cells[3].innerHTML = (tax / 100).toFixed(2);
         cells[5].innerHTML = "$" + (totalWithTax / 100).toFixed(2);
      }

      // add event listener to Submit button
      var submitButton = document.getElementById("sButton");
      if (submitButton.addEventListener) {
        submitButton.addEventListener("click", calcTotal, false);
      } else if (submitButton.attachEvent)  {
        submitButton.attachEvent("onclick", calcTotal);
      }
   </script>
</body>
</html>
```
