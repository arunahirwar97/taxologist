Dropzone.autoDiscover=true;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'/assistance_expert/',
    maxFiles:5,
    maxFilesize:2,
    acceptedFiles:'.jpg',
})