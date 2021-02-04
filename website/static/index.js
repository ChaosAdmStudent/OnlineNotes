function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  } 

  // Fetch is used to send request. We're sending to delete-note endpoint 
  // We're sending a json body 
  // window.location.href ='/' helps to load the home page (reload since we're doing all this on the home page itself)