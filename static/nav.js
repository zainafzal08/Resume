const bs = window.ReactBootstrap;

class myNavbar extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
	  	pages: [
	  	{title: "dic", link: "/dic", subPages: []}
	  	]
    };
  }
  render() {
  	let elems = [];
  	elems.push(
      React.createElement(
        bs.NavItem,
        { eventKey: 1, href: "#" },
        "Link"
      ));
  	elems.push(
      React.createElement(
        bs.NavItem,
        { eventKey: 2, href: "#" },
        "Link"
      ));
    return React.createElement(
    bs.Navbar,
    null,
    React.createElement(
      bs.Navbar.Header,
      null,
      React.createElement(
        bs.Navbar.Brand,
        null,
        React.createElement(
          "a",
          { href: "/" },
          "Zain Afzal"
        )
      )
    ),
    React.createElement(
      bs.Nav,
      null,
      elems
    )
  );
  }
}

// Time to bind our wonderful navbar to the page!
ReactDOM.render(
  React.createElement(myNavbar,null,null),
  document.getElementById('nav')
);