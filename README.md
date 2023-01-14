# THEORY of React 

Hi, welcome to the React Workshop! This should give you a good basic theory of
React that will allow you to pretty much understand everything happening at our
workshop. Maybe a few notes about theory: A theory is not useful in some sense.
It helps us to explain things we see and maybe predict some things. Newton could
explain why an apple fell on his head with his theory and predict bunch of
really useful stuff BUT you cannot build anything usefull with it. You always
need a lot more mechanical engineering concepts for example.

So yeah, this is a THEORY of React and thus you will NOT be able to build
anything useful with this. Or at least I do not expect to. We will show how to
make use of this theory in the workshop! It's is for you the be able to explain
the things that will happen.

## How to read.

Read it like a book (top to bottom, left to right, why am I explaining this).
However, there will be some text that are Links like [ This
](https://www.youtube.com/watch?v=dQw4w9WgXcQ). At this points, you shall follow
the Link (by Clicking it, omg you aint stupid) and come back once you read that
chapter. 

## Guide

First, I would advise you to have a look into [History of Frontend
Devlopment](./history-of-web/history.md) which will help you understand why
things are the way they are and why it will probably not stay that way.

Now, that you know the pain of front end development, we shall introduce the
basics of react, that is how to make simple *components*. For this checkout this
chapter about [React Components](./react-basics/components/components.md).

We should know be able to understand the understand the relationship between
React components and HTML elements. But you may remember the HTML element

```html
<img src="some url"/>
```

Well this looks different than a normal `<div>` because it takes a weird thingy 
`src` which you can assign an url to. Learn more about it in the chapter about
[Properties](./react-basics/props/props.md).

Great, we know how to make things really reusable now by putting it into
components and pass around properties. BUT you are not done. There is more to
it. For example, we can control how things are rendered for the user. This could
be really usefull to create interesting website. Check it out in the chapter
about [Rendering](./react-basics/rendering/rendering.md).

If you reached this point, you should pretty much have a good understanding of
the way react takes a component and makes HTML out of it. However, I promised
that react is actually about State management and that changes to the State
would *magically* apply changes to our components. For this we will first
introduce the concept of [Hooks](./react-basics/hooks/hooks.md).

Nice now we can rerender HTML according to the state of our app/website. BUT
where do we get the data from?? Probably from the internet, or more specifically
from our backend server. Hence, we need to talk about how to get data 
in our [Data Fetching](./react-basics/fetching/fetching.md) chapter.

You made it! You reached the End-Game. This last section will connect
everything. In the beginning, we always assumed that somehow, we just have some
data on the user's browser already. We used that data to inject it into the
components. This cannot be true because **Where did the data came from?**. 
Later we used Hooks to connect data (the State of our App) to the rendering
process of our website. But still, data was still somehow there. Then we talked
about how to get the dat, but .... **What do you do with that data?** Now, we
will finally make this connection.  That is, we connect data fetching with react
hooks! This is what WebDevelopment is all about. Getting data and make it look
nice! I will explain it in the chapter about [Combining Fetching and
Displaying](./react-basics/fetching/display.md).