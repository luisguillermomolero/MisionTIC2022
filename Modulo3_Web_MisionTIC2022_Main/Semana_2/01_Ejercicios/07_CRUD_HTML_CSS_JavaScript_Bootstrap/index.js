function loadTable() {
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "https://www.mecallapi.com/api/users");
    xhttp.send();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
        var trHTML = ''; 
        const objects = JSON.parse(this.responseText);
        for (let object of objects) {
          trHTML += '<tr>'; 
          trHTML += '<td>'+object['id']+'</td>';
          trHTML += '<td><img width="50px" src="'+object['avatar']+'" class="avatar"></td>';
          trHTML += '<td>'+object['fname']+'</td>';
          trHTML += '<td>'+object['lname']+'</td>';
          trHTML += '<td>'+object['username']+'</td>';
          trHTML += '<td><button type="button" class="btn btn-outline-secondary" onclick="showUserEditBox('+object['id']+')">Edit</button>';
          trHTML += '<button type="button" class="btn btn-outline-danger" onclick="userDelete('+object['id']+')">Del</button></td>';
          trHTML += "</tr>";
        }
        document.getElementById("mytable").innerHTML = trHTML;
      }
    };
  }
  
  loadTable();

  function showUserCreateBox() {
    Swal.fire({
      title: 'Crear Usuario',
      html:
        '<input id="id" type="hidden">' +
        '<input id="fname" class="swal2-input" placeholder="Nombre">' +
        '<input id="lname" class="swal2-input" placeholder="Apellido">' +
        '<input id="username" class="swal2-input" placeholder="Username">' +
        '<input id="email" class="swal2-input" placeholder="Correo">',
      focusConfirm: false,
      preConfirm: () => {
        userCreate();
      }
    })
  }
  
  function userCreate() {
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
      
    const xhttp = new XMLHttpRequest();
    xhttp.open("POST", "https://www.mecallapi.com/api/users/create");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "fname": fname, "lname": lname, "username": username, "email": email, 
      "avatar": "https://www.mecallapi.com/users/cat.png"
    }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      }
    };
  }

  function showUserEditBox(id) {
    console.log(id);
    const xhttp = new XMLHttpRequest();
    xhttp.open("GET", "https://www.mecallapi.com/api/users/"+id);
    xhttp.send();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        const user = objects['user'];
        console.log(user);
        Swal.fire({
          title: 'Editar Usuario',
          html:
            '<input id="id" type="hidden" value='+user['id']+'>' +
            '<input id="fname" class="swal2-input" placeholder="Nombre" value="'+user['fname']+'">' +
            '<input id="lname" class="swal2-input" placeholder="Apellido" value="'+user['lname']+'">' +
            '<input id="username" class="swal2-input" placeholder="Username" value="'+user['username']+'">' +
            '<input id="email" class="swal2-input" placeholder="Correo" value="'+user['email']+'">',
          focusConfirm: false,
          preConfirm: () => {
            userEdit();
          }
        })
      }
    };
  }
  
  function userEdit() {
    const id = document.getElementById("id").value;
    const fname = document.getElementById("fname").value;
    const lname = document.getElementById("lname").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
      
    const xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "https://www.mecallapi.com/api/users/update");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "id": id, "fname": fname, "lname": lname, "username": username, "email": email, 
      "avatar": "https://www.mecallapi.com/users/cat.png"
    }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      }
    };
  }

  function userDelete(id) {
    const xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "https://www.mecallapi.com/api/users/delete");
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ 
      "id": id
    }));
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4) {
        const objects = JSON.parse(this.responseText);
        Swal.fire(objects['message']);
        loadTable();
      } 
    };
  }