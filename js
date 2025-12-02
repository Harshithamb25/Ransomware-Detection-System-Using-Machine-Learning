let person = {
  name: 'hii',
  domain: 'cyber',
  greet: function() {
    return 'hello ' + this.name;
  }
};

console.log(person.greet()); // Output: hello hii
