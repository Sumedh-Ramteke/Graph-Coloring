function color_australia() {
    fetch(`/get_australia_color`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        color_map(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

function color_map(colors){
    var wa = document.getElementById('AU-WA');
    wa.style.fill = colors['Western Australia'];
    
    var nt = document.getElementById('AU-NT');
    nt.style.fill = colors['Northern Territory'];

    var qld = document.getElementById('AU-QLD');
    qld.style.fill = colors['Queensland'];

    var sa = document.getElementById('AU-SA');
    sa.style.fill = colors['South Australia'];

    var nsw = document.getElementById('AU-NSW');
    nsw.style.fill = colors['New South Wales'];

    var vic = document.getElementById('AU-VIC');
    vic.style.fill = colors['Victoria'];

    var tas = document.getElementById('AU-TAS');
    tas.style.fill = colors['Tasmania'];
}

color_australia();  