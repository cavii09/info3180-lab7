<template>
    <form @submit.prevent="uploadPhoto" id="uploadForm"> 
    <div>
       <span v-if="uploads">File Upload Successful</span>
       <li v-for="upload in uploads" class="images"></li>  
       <label class="description" for="description">Description</label>
       <input type="text" id="description" name="description"><br>

        <label class="photo" for="photo">Photo</label>
       <input type="file" id="photo" name="photo"><br>
       <button class="btn btn-primary mb-2" id="Submit" name="Submit">Submit</button>
    </div>
        </form>
</template>

<script>
export default {
      data() {
        return {csrf_token: ''}
      },
      
      created() {
          this.getCsrfToken();
      },
      methods: { uploadPhoto(){
      
      let uploadForm = document.getElementById('uploadForm');
      let form_data = new FormData(uploadForm);
        
      fetch("/api/upload", {
       method:'POST',
       body: form_data,
       headers: {
          'X-CSRFToken': this.csrf_token
       }  
      })
        .then(function (response) {
           return response.json();
        })
        .then(function (data) {
         // display a success message
           console.log(data);
        })
        .catch(function (error) {
           console.log(error);
        })
      }, 
         getCsrfToken() {
         let self = this;
         fetch('/api/csrf-token')
         .then((response) => response.json())
         .then((data) => {
           console.log(data);
           self.csrf_token = data.csrf_token;
          })
         },  
         
      }       
};

</script>
