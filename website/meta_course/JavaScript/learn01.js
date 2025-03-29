var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink'];

listArrayItems(colors);

function listArrayItems(arr) {
    for (var i = 0; i < arr.length; i++) {
        // Use ternary operator to check for 'pink' and apply 'black' font color
    /* var bg_color = arr[i]
    if (textColor == 'pink') {
        var bg_color = arr[i-1];}
    */
    var textColor = arr[i] === 'pink' ? 'black' : arr[i];

        var styles = `font-size: 40px; border-radius: 10px; border: 1px solid blue; background: pink; color: ${textColor}`;
        console.log("%c"+ (i+1) + " " + arr[i], styles); // Display each array item in its respective color
    }
}

