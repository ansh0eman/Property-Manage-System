const propertyList = document.querySelector('.property-list');
const tabLinks = document.querySelectorAll('.tab-link');
const tabContents = document.querySelectorAll('.tab-content');
const propertySelect = document.querySelector('#property');
const bookingForm = document.querySelector('#booking-form');
const userAuthForm = document.querySelector('#user-auth-form');

// Sample property data
const properties = [
    {
        id: 1,
        title: 'Property 1',
        image: 'https://via.placeholder.com/300x200',
        price: 100
    },
    {
        id: 2,
        title: 'Property 2',
        image: 'https://via.placeholder.com/300x200',
        price: 200
    },
    {
        id: 3,
        title: 'Property 3',
        image: 'https://via.placeholder.com/300x200',
        price: 300
    },
    {
        id: 4,
        title: 'Property 4',
        image: 'https://via.placeholder.com/300x200',
        price: 400
    },
    {
        id: 5,
        title: 'Property 5',
        image: 'https://via.placeholder.com/300x200',
        price: 500
    }
];

// Function to generate property items
const generatePropertyItems = () => {
    properties.forEach(property => {
        const propertyItem = document.createElement('div');
        propertyItem.classList.add('property-item');

        const propertyImage = document.createElement('img');
        propertyImage.classList.add('property-image');
        propertyImage.src = property.image;
        propertyItem.appendChild(propertyImage);

        const propertyInfo = document.createElement('div');
        propertyInfo.classList.add('property-info');
        propertyInfo.textContent = property.title;
        propertyItem.appendChild(propertyInfo);

        propertyList.appendChild(propertyItem);
    });
};

// Function to switch tabs
const switchTab = (event) => {
    tabLinks.forEach(link => link.classList.remove('current'));
    event.target.classList.add('current');

    tabContents.forEach(content => content.classList.remove('current'));
    document.querySelector(event.target.dataset.tab).classList.add('current');
};

// Function to generate property options
const generatePropertyOptions = () => {
    properties.forEach(property => {
        const propertyOption = document.createElement('option');
        propertyOption.value = property.id;
        propertyOption.textContent = property.title;
        propertySelect.appendChild(propertyOption);
    });};

// Function to handle user authentication form submission
const handleUserAuthFormSubmit = (event) => {
    event.preventDefault();

    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;

    // Validate user credentials
    if (email === 'user@example.com' && password === 'password') {
        alert('Login successful!');
    } else {
        alert('Invalid email or password.');
    }
};

// Function to handle booking form submission
const handleBookingFormSubmit = (event) => {
    event.preventDefault();

    const propertyId = document.querySelector('#property').value;
    const guests = document.querySelector('#guests').value;
    const checkin = document.querySelector('#checkin').value;
    const checkout = document.querySelector('#checkout').value;

    // Validate booking data
    if (propertyId && guests && checkin && checkout) {
        alert(`Booking successful! Property: ${propertyId}, Guests: ${guests}, Check-in: ${checkin}, Check-out: ${checkout}`);
    } else {
        alert('Please fill in all required fields.');
    }
};

// Generate property items
generatePropertyItems();

// Generate property options
generatePropertyOptions();

// Add event listeners for tab switching
tabLinks.forEach(link => link.addEventListener('click', switchTab));

// Add event listener for user authentication form submission
userAuthForm.addEventListener('submit', handleUserAuthFormSubmit);

// Add event listener for booking form submission
bookingForm.addEventListener('submit', handleBookingFormSubmit);