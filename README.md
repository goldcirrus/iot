<html>
<head> 
  
</head>  
  
<body>


<p id="a">display 1</p>
  <p id="b">display 2</p>




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
  
  var dbRef = firebase.database().ref().child('test');
  dbRef.on('value', snap=>document.getElementById('a').innerHTML=snap.val());
  
  var starRef = firebase.database().ref('dht');
  starRef.on('value', (snapshot)=>{
                          var data = snapshot.val();
                          document.getElementById('b').textContent = data;
                        });
  
  
  
  </script>

 


  


    
   

  </body>
  </html>



