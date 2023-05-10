
function changeImage() {
    var Image_Id = document.getElementById('myImage');
    if (Image_Id.src.match("a.jpg")) {
        Image_Id.src = "b.jpg";
    }
    else {
        Image_Id.src = "a.jpg";
    }
}        
