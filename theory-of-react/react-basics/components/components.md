# React components

Alright, you are know at the chapter about react components. In a nutshell, a
react component is the way we create "custom elements in HTML" (metaphorically
speaking). For example, how cool would it be, if we can simple use something
like this

```html
<InstagramPost />
```

in HTML to easily have an element looking like this

<img src="./assets/component.png" /> 

with all the data and functionality like for example the Like button. Sadly, it's
a little bit more complicated.

## Functional Components

What is a function? In Javascript a function looks something like this, I will 
not go into the details here...

```javascript
function I_am_a_function() {

}
``` 

to make it a function component, we **change the file ending to .jsx or .tsx** AND
return some HTML in that function. For example, if the example from above is saved
in a file named `TestFunction.js` we would rename that file to `TestFunction.jsx`
and then change the function to look like this (actually, we may have to do more
than just this but we will address it in later chapters + the workshop):

```javascript
function I_am_a_function() {
    return (
        <div>
            I am a function component!
        </div>
    )
}
``` 

Note that I put the text `I am a function component!` inside a `div`. This is really important
as a function component must **ALWAYS return exactly ONE** element (in HTML sense).

This is not valid as it is not an element:

```javascript
function I_am_a_function() {
    return (
        I am a function component!
    )
}
``` 

This is valid, as we return one element, which consists of nested elements. Still, its only one element.

```javascript
function I_am_a_function() {
    return (
        <div>
            <h1>
                LOOL
            </h1>
            <h2>
                I am a function component!
            </h2>
        </div>
    )
}
``` 

Whenever we know use `<I_am_a_function />` in React, it will then render to

```html
<div>
    <h1>
        LOOL
    </h1>
    <h2>
        I am a function component!
    </h2>
</div>
```
 
in our browser. I will just leave it a black box how react actually does that
but it works.

Yeah, it's that simple.

## Why components are not that bad

Sofar, it was quite simple to understand but we have yet to see the advantage of
react since it would have been much simplier to just .... write that stupid html
in the first place and just copy paste it everytime we need it.

The advantage of components is that, we now can separate this simple element 
from its use.  Imagine the manager comes around and says HTML from above must
say LOOOL (with 3 O's) because otherwise we will not hit our revenue target and
I have to sleep for dinner because no money no food :(.  Would you like to go to
every place where you placed that LOOL?  Of course not, with components you
simple go into the component and change it there.  Than, everywhere you use
`<I_am_a_function />` should have that update automatically.  This is why they
are usefull.

## Thinking in components

This one is a little bit trickier. But the generally rule is: 

**If you want reuse it, make it a component!**

That means, when you have that part of HTML occuring somewhere twice, better
make it a component (which makes sense as I discussed before). Often, 
people will also make things a component when they think, it is nice to 
group them.

For example, almost every website as some sort of a header. For github the
header looks somewhat like this.

<img src="./assets/header.png">

So obviously, the header will only occure once on that page but still, people
would make it a component to group the single elements to a single component.
It's just looks nicer in the code! Another golden rule:

**If it helps to keep the code clean, make it a component!**


## Getting data into components?

This will refer to the task from our manager. We may know that this guy really 
like the 'O' and could comeback to us tomorrow and ask us to add another 'O' 
to the text... 

One solution we may come up is to take the `LOOL` out of that function itself,
and put it somewhere else such that we dont have to fiddle with HTML in 
that function component everytime. It may look like this.

```javascript
const my_boss_likes_big_O_and_he_cannot_lie = "LOOOL";

function I_am_a_function() {
    return (
        <div>
            <h1>
                {my_boss_likes_big_O_and_he_cannot_lie}
            </h1>
            <h2>
                I am a function component!
            </h2>
        </div>
    )
}
``` 

Now everytime he comes around, we can change the text in
`my_boss_likes_big_O_and_he_cannot_lie` without accidentally breaking the HTML
where our text `LOOL` was before that. Yeah, obviously this is a somewhat stupid
example but I just wanted to show that that you can use `{name_of_the_variable}`
to inject data into the HTML!

That's it for function components!