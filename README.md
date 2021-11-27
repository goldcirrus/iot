<html>
<head> 
  
</head>  
  
<body>

<p>temperature is: </p>
<p id="d"></p>
<p>humidity is: </p>
<p id="e"></p>




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
  
  
  var dhtRef = firebase.database().ref().child('sensor');

               //listen child_added
  dhtRef.on('child_added', (data) => {
               addElement(data.key, data.val());
        });

        function addElement(key,dataObject){
              document.querySelector('#d').innerHTML=dataObject.temp;
              document.querySelector('#e').innerHTML=dataObject.humidity;
        }
  
  </script>

  </body>
  </html>



