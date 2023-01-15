# Rendering

Wait! You promised that React would take care of rendering!! It does. But you
still have to help it render it the way you want. We first look into conditional
rendering, than we look into a more general way how things can be rendered.

## Conditional Rendering

Back to our story, after we finally got our components and properties right, we
were almost promoted to senior engineer which means more MONEY. There is like,
only one little task left. We have to build a login/logout button. This button
should say Login, if we are logout, and logout, if we are log in.  Again, we
will be building the component while other use it. This time, we spent time
reading the react docs to get the solution right straight away.

```javascript
function LoginButton(props) {
    // note that we destruct props 
    const {isUserLogIn} = props;
    // isUserLogIn == true, means we are Log in!
    if (isUserLogIn == true) {
        return (
            <button>Logout</button>
        )
    } 
    // isUserLogIn == false means we are Logout
    else if (isUserLogIn == false) {
        return (
            <button>Login</button>
        )
    }
}
```
Note that there is a `if, else` here, hence conditional rendering because
we render different buttons based on whatever `props.isUserLogIn` is.

For example, `<LoginButton isUserLogin={true} />` would produce
`<button>Logout</button>`

> Trivia: You could also use `<LoginButton isUserLogin />` which is the same as
`<LoginButton isUserLogin={true} />` because it is a boolean. However,
`<LoginButton />` is not the same as `<LoginButton isUserLogin={false} />`.
Yeah, fuck javascript.

Well, you may guess it, we can even make the `LoginButton` look more sexy using
the tenary operator.

```javascript
function LoginButton(props) {
    // note that we destruct props 
    const {isUserLogIn} = props;
    return (
        {isUserLogin == true ? 
            (<button>Logout</button>) 
        : 
            (<button>Login</button>) 
        }
    )
}
```
See what I did there? I used the concept that we can inject data using `{}` but
I injected javascript. Using the tenary operator `condition ? () : ()` this can
be shortened by a lot! Again, just to make it look nice. BUT it really makes you
realize that we can actually render anything we want by now!

## Rendering anything we want

Yeah, using the notion that we can use javascript inside `{}` kinda implies that
we have a lot of possibilies to render items now. For example, we could 
render an array passed to use as `props`. 

```javascript
function ShowArray(props) {
    const {listOfNumbers} = props;
    return (
        <div>
            {listOfNumbers.map((item) => <p>{item}</p> )}
        </div>
    )
}
```

You see what I did there? I pass in the `.map` function into the `{}`. This
function (you should look it up online `Array.map`) will map each element in the
list to `<p>{item}</p>` and WHAT? yes we just mapped `item` to `{item}` again.
React does this mapping stuff in a nested way all day long. For example, if we
use that `<ShowArray lisOfNumbers={[1,2,3]} />`, our component would render to
this

```
<div>
    <p>1</p>
    <p>2</p>
    <p>3</p>
</div>
```

Yeah, we rendered enough stuff for now.