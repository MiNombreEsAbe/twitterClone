// JS for posts page

$(() => {
    // Detect when a user clicks on any of the menu icons
    $('.jsMenuIcon').click(function () {
        // Toggle the display of the popup box
        $(this).next('div').toggle(); 
    });
});