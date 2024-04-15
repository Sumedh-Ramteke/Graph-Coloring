function color_india() {
    fetch(`/get_india_color`)
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
    var state = document.getElementById('INAN');
    state.style.fill = colors['Andaman and Nicobar Islands'];
    
    state = document.getElementById('INTG');
    state.style.fill = colors['Telangana'];

    state = document.getElementById('INAP');
    state.style.fill = colors['Andhra Pradesh'];

    state = document.getElementById('INAR');
    state.style.fill = colors['Arunachal Pradesh'];

    state = document.getElementById('INAS');
    state.style.fill = colors['Assam'];

    state = document.getElementById('INBR');
    state.style.fill = colors['Bihar'];

    state = document.getElementById('INCH');
    state.style.fill = colors['Chandigarh'];

    state = document.getElementById('INCT');
    state.style.fill = colors['Chhattisgarh'];

    state = document.getElementById('INDH');
    state.style.fill = colors['Dadra and Nagar Haveli and Daman and Diu'];

    state = document.getElementById('INDL');
    state.style.fill = colors['Delhi'];

    state = document.getElementById('INGA');
    state.style.fill = colors['Goa'];

    state = document.getElementById('INGJ');
    state.style.fill = colors['Gujarat'];

    state = document.getElementById('INHR');
    state.style.fill = colors['Haryana'];

    state = document.getElementById('INHP');
    state.style.fill = colors['Himachal Pradesh'];

    state = document.getElementById('INJH');
    state.style.fill = colors['Jharkhand'];

    state = document.getElementById('INKA');
    state.style.fill = colors['Karnataka'];

    state = document.getElementById('INKL');
    state.style.fill = colors['Kerala'];

    state = document.getElementById('INMP');
    state.style.fill = colors['Madhya Pradesh'];

    state = document.getElementById('INMH');
    state.style.fill = colors['Maharashtra'];
    
    state = document.getElementById('INMN');
    state.style.fill = colors['Manipur'];
    
    state = document.getElementById('INML');
    state.style.fill = colors['Meghalaya'];

    state = document.getElementById('INMZ');
    state.style.fill = colors['Mizoram'];

    state = document.getElementById('INNL');
    state.style.fill = colors['Nagaland'];

    state = document.getElementById('INOR');
    state.style.fill = colors['Odisha'];

    state = document.getElementById('INPY');
    state.style.fill = colors['Puducherry'];

    state = document.getElementById('INPB');
    state.style.fill = colors['Punjab'];
    
    state = document.getElementById('INRJ');
    state.style.fill = colors['Rajasthan'];

    state = document.getElementById('INSK');
    state.style.fill = colors['Sikkim'];

    state = document.getElementById('INTN');
    state.style.fill = colors['Tamil Nadu'];

    state = document.getElementById('INTR');
    state.style.fill = colors['Tripura'];

    state = document.getElementById('INUP');
    state.style.fill = colors['Uttar Pradesh'];

    state = document.getElementById('INUT');
    state.style.fill = colors['Uttarakhand'];

    state = document.getElementById('INWB');
    state.style.fill = colors['West Bengal'];

    state = document.getElementById('INLD');
    state.style.fill = colors['Lakshadweep'];

    state = document.getElementById('INJK');
    state.style.fill = colors['Jammu & Kashmir'];

    state = document.getElementById('INLA');
    state.style.fill = colors['Ladakh'];

    state = document.getElementById('INDL');
    state.style.fill = colors['Delhi'];
}

color_india();  