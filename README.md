<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  
<script>
$(document).ready(function(){
  $("button").click(function(){
    $(this).alert("test");
  });
});
</script>
  
  
  
</head>  
  
  <body>

<p id="test">This is some <b>bold</b> text in a paragraph.</p>
<p id="a">paragraph 2</p>

<button id="btn1">button1</button>
<button id="btn2">button2</button>


<script src="https://www.gstatic.com/firebasejs/7.6.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/7.6.1/firebase-database.js"></script>
<script>
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyAglzGoqKSJiCL3HZhP3jFcJHsrKGkKgZc",
    authDomain: "iot2021-94458.firebaseapp.com",
    databaseURL: "https://iot2021-94458-default-rtdb.firebaseio.com",
    projectId: "iot2021-94458",
    storageBucket: "iot2021-94458.appspot.com",
    messagingSenderId: "207386797843",
    appId: "1:207386797843:web:6a5630406c3e429c8c9ce6",
    measurementId: "G-29LJLQPN7L"
  };

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  var dbRef = firebase.database().ref().child('sensor').child( );
  dbRef.on('value', snap=>document.getElementById('a').innerHTML=snap.val());

 


  //document.getElementById("a").innerText = dataX;

</script>
  
  
  <script type="module">
   //Copy and paste these scripts into the bottom of your <body> tag, but before you use any Firebase services:

  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.5.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.5.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyAglzGoqKSJiCL3HZhP3jFcJHsrKGkKgZc",
    authDomain: "iot2021-94458.firebaseapp.com",
    databaseURL: "https://iot2021-94458-default-rtdb.firebaseio.com",
    projectId: "iot2021-94458",
    storageBucket: "iot2021-94458.appspot.com",
    messagingSenderId: "207386797843",
    appId: "1:207386797843:web:6a5630406c3e429c8c9ce6",
    measurementId: "G-29LJLQPN7L"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
    
    $(document).ready(function(){
  $("p").click(function(){
    $(this).append("some text appended+");
    $(this).append(analytics);
  });
});
    
</script>
    
   

  </body>
  </html>

llll
Welcome to GitHub Pages

