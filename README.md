<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  
<script>
$(document).ready(function(){
  $("p").click(function(){
    $(this).alert("test");
  });
});
</script>
</head>  
  
  
<body>
   <p id="a">test </p>
  
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
</script>
    
   

  </body>
  </html>

llll
Welcome to GitHub Pages

