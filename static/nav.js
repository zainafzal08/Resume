class NavBar extends React.Component {
  render() {
  	
    return React.createElement('h1',null,'Hello, world!');
  }
}

// Time to bind out wonderful navbar to the page!
ReactDOM.render(
  React.createElement(NavBar,null,null),
  document.getElementById('nav')
);