# Properties

I have already introduce that properties are somewhat weird as they look a
little bit different than our normal HTML element. However, they are really
usefull. But first, I will introduce an use case for them.

Since, we manage to get the 'O' right and not get fired from the company, we
face the next challenge: We have to create a simple Greeting text for our user.
We ideally want to put this in a component, because well, it will be used in
BUNCH of placed. Also our company has such a big success that we now have like,
idk, 10000 engineers working at this simple software \*hust\* twitter \*hust\*.
Because of that, our team split up the task and we should be doing the component
while others work on how to get the name of the user.

We may come up with a solution like this with our current knowledge.

```javascript
let username = "Placeholder";
function Greeting() {
    return (
        <p>
            Hello {username} <3
        </p>
    )
}

```

We happily submit this solution and a hour later, the boss calls us into his
office because the other engineers told him we dont know how to Code.

## What went wrong??

Well it is a little bit more to it. We want to use the `<Greeting />` component
in various places BUT, well, it will always say `Hello Placeholder <3`.  You can
argue that the other engineers should stop crying and change the `username`
variable. But this is NOT how to do it. It's a stupid solution (I dont even know
if it would work) that would make it more difficult... What we want it something
similar to what the `<img />` element in HTML already can!

So we want something like this `<Greeting username="John" />`. This way, we can
focus on making the `Greeing` components while others can use it by just pluging
in the `username` **Property**.

## React Properties

We could come up with this solution that uses properties:

```javascript
function Greeting(props) {
    return (
        <p>
            Hello {props.username} <3
        </p>
    )
}
```

Yeah, that's it... Note that our function now takes an argument `props`. We
could have named it anything we want but `props` is like how everybody does it.
In our HTML we can then use `props` to get to the `username`.

This looks simple, BUT it can quickly fuck your code up. Why? Because we may 
have not communicate it well with others on what `props` we actually accept.  A
developer may think, he can use `<Greeting user="John" />` while another one
thinks it is `<Greeting user_name="John" />`. None of this would work AND there 
is no solution to that but just tell them somehow to use `<Greeting
username="John" />`. (There is a solution which is Typescript).

### Props under the hood

What is this magical props thing? Well it is just a Javascript object!
You can create javascript objects like this.

```javascript
const obj = {
    some_nubmer_field: 32, // access it by obj.some_number_field 
    some_string_field: "hello", // access it by obj.some_string_field 
    some_boolean_field: true, // access it by obj.some_boolean_field 
    some_array_field: [1,2,3,4] // access it by obj.some_array_field 
    ....
}
```

With that we know, why we could do `props.username`. Because React will
take every Property we throw in the component  (here e.g. username, age, sex)

`<Greeting username=".." age=29 sex="female" />`

and make it a field in our `props` object.

## Getting data into props

Okay, this is going into more advanced stuff. We are now combining two ideas,
that we are able to inject data to a HTML and properties. Have a look at this
based on our `<Greeting />` component:

```javascript
const user = "John";
function HomePage(){
    return (
        <div>
            <Greeting username={user} />
        </div>
    )
}
```

Notice what happened? We used the idea that we can inject data by using the `{}`
but we inject it into the props! You surely can image that `<Greeting />` may
even use our injection to injected it into the props of a nested component -
**Props-ception**!

Some trivia, we can to a lot of things inside the `{}`, actually everything
Javascript can do. For example, we could do:

```javascript
const user = "John";
function HomePage(){
    return (
        <div>
            <Greeting username={user + "!"} />
        </div>
    )
}
```

which would be equal to `<Greeting username="John!" />>`

## Destructing props

No why would you want to break props? They are so helpful! No worries,
destructing means something different here. Imagine we have like a lot of props
fields. For example: 

`<Greeting username="Lana" age=29 sex="female" />`

Well, we would need to `props.username, props.age, props.sex` to access it which
is like, idk, programmers dont like to repeat themselves. Here we repeated like 
`props` three times... A solution to it would be to write the component like
this: 

```javascript
function Greeting(props) {
    // we destruct props like this:
    const {username, age, sex} = props;
    return (
        <p>
            Hello {username}. You are {age} years old and {sex}.
        </p>

    )
}
```

Note that we effectively pulled out the fields of that props so that we can use
them later. Yeah, it does not changes anything in behaviour. Just looks better.
It's like that fancy coffee barista that pours a nice heart into your coffee.
It tastes the same but at least you know that someone loves you... Yeah, coding
is pretty much the same. 

<img src="./assets/coffee.png" />

That should be it. Maybe have a coffee break!