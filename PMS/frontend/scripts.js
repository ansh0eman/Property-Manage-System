const propertyList = [
    {
      title: "Property 1",
      description: "This is Property 1",
    },
    {
      title: "Property 2",
      description: "This is Property 2",
    },
    {
      title: "Property 3",
      description: "This is Property 3",
    },
  ];
  
  const propertyListing = document.getElementById("property-list");
  const propertyDetails = document.getElementById("property-details");
  const propertyTitle = document.getElementById("property-title");
  const propertyDescription = document.getElementById("property-description");
  const bookPropertyButton = document.getElementById("book-property");
  
  propertyListing.addEventListener("click", (event) => {
    if (event.target.tagName === "LI") {
      const property = propertyList.find(
        (prop) => prop.title === event.target.innerText
      );
      displayPropertyDetails(property);
    }
  });
  
  bookPropertyButton.addEventListener("click", () => {
    // Handle booking logic here
    console.log("Book Property");
  });
  
  function displayPropertyDetails(property) {
    propertyDetails.hidden = false;
    propertyTitle.innerText = property.title;
    propertyDescription.innerText = property.description;
  }
  
  const searchBox = document.getElementById("search-box");
  searchBox.addEventListener("input", (event) => {
    const searchTerm = event.target.value.toLowerCase();
    const filteredProperties = propertyList.filter(
      (property) => property.title.toLowerCase().includes(searchTerm)
    );
    displayProperties(filteredProperties);
  });
  
  function displayProperties(properties) {
    propertyListing.innerHTML = "";
    properties.forEach((property) => {
      const li = document.createElement("li");
      li.innerText = property.title;
      propertyListing.appendChild(li);
    });
  }
  
  displayProperties(propertyList);