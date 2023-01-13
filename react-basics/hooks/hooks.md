# Hooks

This is a strage place in React. I like to show a weird example first to show
you why Hooks have been invented. 

```javascript
function Component() {
    let counter;
    return (
        <button onClick={() => counter += 1} >{counter}</button>
    )
}
```

Soooo, long shot. If we click this button, we would increment the variable
`counter` by one. What do you think would happen when we display it with
`{counter}` as we do it inside the button. You would think, *Well, it should
also update to be the new value!*. This is why we used React in the first
place, didnt we? Haha Facebook sends their regards! Of course it does not work
this way.

This is why we need Hooks! To connect **Data that changes to the change we want
to make in the HTML**. I will introduce the most common Hooks! Funny enough,
Facebook sold React as the solution to handle this specific issue in the first
place but it does not do it out-of-the-box. What a shame...

## The useState Hook

This one is like, idk, the most popular one. It makes a function component have
a state. Everytime the State changes, React will take care of changing the HTML
accordingly (finally...). Let me give you a metaphor for it: 

Imagine your Room is idk, a React component. You have a light switch in your
room, so everytime you hit the switch, you obviouly change it's state to on or
off. But you dont simply change the state, your lamp will also make light or
not, depending on the state. This is pretty much what useState does. It changes
the HTML depending on the State to make them tightly coupled.

With that we can fix the example from above.

```javascript
function Component() {
    let [counter, setCounter] = useState(0);
    return (
        <button onClick={() => setCounter(counter+1)} >{counter}</button>
    )
}
```

What is going on here? We use `useState(0)` to get a state. Then we destruct the
state into the variables `counter` and `setCounter`. The variable `counter` will
be intially `0` because we said so in the `useState(0)`. The `setCounter`
variable is actually a function and can be used to, well, set the variable
`counter` to a new value. 

You may think: This is stupid. Why does React not do it automatically? Why do I
have to wrap it in useState? YES YES. 

<img src="https://i.imgflip.com/77dy2s.jpg" width="400"/>

It's just because React sucks. There are other frontend frameworks that can do
this!

## The useEffect Hook

Well, the useEffect Hook is in a weird place. It's kinda useless most of the
time.  But you need it once in a while. At this point you should go back to the
main book page and come back to this once you read the section about data
fetching. 