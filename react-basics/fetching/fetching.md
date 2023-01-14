# Data Fetching

At this point we are getting the intersection to our backend! Thus I will
shortly explain the concept of backend, for frontend developers.

## The black-box backend

As Frontend-Engineers, our job is to make to buttons and text look nice.
However, sometimes we also have to spent time on getting data from the backend
to the user's browser and then make it look nice, too. To make it less abstract:

Imagine you would want to invent Facebook. Obviously, you would want to collect
all kind of data about your users: their age, sex, name, friends, phone
contacts, emails, photos, location, text messages with friends, political
orientation, and more! Most of that, you will save it for analysis (and for
profit) later. BUT some of it can also be shared with the users! For example,
users would surely love to see some of the photos of their friends. Where do you
store that data? In your Backend!

### Fishing for data 

It's actually not obvious how a browser gets its data! And it would probably
also take too long (and maybe confusing?) to explain it in a precise manner.
Hence, I will explain it with a metaphor: Fishing!

So when you go fishing, you use obviously have to use some sort of bait.
Depending on the bait, you catch different kind of fish. Yeah, that's how you
get data from your backend! Your backend developers provide different kind of
'fish' and tell you what bait you have to use to get them. All you have to do is
use the right bait and you get the fish you want.

**So how does the bait look like?** Depends on your backend! There are various
concept with REST and Graphql probably the most popular ones. It's like having
different brands of bait manufacturers. They kinda look different, maybe they
even perform different, but in the end, you can still catch the fish with both.
We will discuss Graphql later as we need it for the project!

**How does my fish look like?** That also depends on your backend! A Very
popular data representation is JSON, but people also use XML (and more). I would
say that an american carp looks different than an asian carp, too, but I'm no
expert in fishing. However, there is one thing I know for sure: They both taste
good and look similar when served!  Hence, you can do pretty much the same with
any data representation and make a beautiful website as well as you can  serve a
great dish with different kind of fish. We shall look into how graphql does this
later! 

Thus I shall answer the questions: What does GraphQL ('fish bait') look like?
How does the data ('fish') look like? And How do I make use of it in my web app in
React ('how do you cook the fish')?

If you like to know more about how this is actually done, I surely can explain
on our workshop! However, I will stick with that metaphor to make it easily
digestible.

## GraphQL

Well, graphql is kind of like high engineered bait where you can get really
nice fish that are the exact weight you want! You want a 5kg fish? You get
it! There is no way that you get more. That's great since you may not want to
pull out a shark while fishing for crabs.

> GraphQL helps us to prevent overfetching. Overfetching happens when you
request more data from your Backend than you actually need. This is especially
useful for mobile apps because mobile internet connections are slow and expensive!

We will have a look into the ApolloClient, which is a very popular GraphQL
client (kinda of a very popular fishbait manufacturer).

### Queries

In GraphQL you make queries that describes the data that you want. Sounds
confusing, but it's very simple. For example, let assume we want to build a
Tinder for dogs! 

<img src="./assets/dogs.png">

So you may need the dogs name, age, sex, breed, its profile description and some
pictures to show a profile right? GraphQL makes it extremely easy to express it.

```javascript
const dogo_profile = gql`
    query GetDogoProfile {
        dogos {
            name, 
            age,
            sex,
            breed,
            profileDescription,
            selfies {
                url
            }
        }
    }
`;


```

So what just happened? We created a query named `GetDogoProfile` and stored it
in `dogo_profile`. This query, when executed, will be handled by our backend
server and it will hopefully return all the information we requested inside the
`GetDogoProfile {...}`. The backend may respond with

```json
{
"data": {
    "dogos": [
        {
            "name": "Oscar",
            "age": 7,
            "sex": "male",
            "breed": "Golden Retriever",
            "profileDescription": "Woof Woof. Some one wants to go to the park with me?",
            "selfies": [
                {
                    "url" : "https://tinder4dogos.com/pb/oscar_pic_1.jpg",
                },
                {
                    "url" : "https://tinder4dogos.com/pb/oscar_pic_2.jpg",
                },
            ]
        }
    ] 
}
}
```

The first observation is: **We did not overfetch a single bit!**. This data holds
all and only the information that we need! However, you may wonder, why does
`selfies` look that much different than the others? Sadly, in GraphQL it is not
obvious that `selfies` will look like this. (This is where we need types).

Therefore, I will ignore that fact that for now as we will work on it during the
workshop! For the theory it is only important to realize, that the way we write
queries will closely reflect our data outcome (as you can see)!

> Do be confused on why we return `url: ...` for the selfies. It is very common
that you use GraphQL to return urls to bigger files such as pictures, audio or
videos, since you will have a hard time to get them through GraphQL and because of
performance reasons.

### Query arguments

For example, in Tinder you often filter by sex. Maybe our dog Oscar is 
interested in female dogs. Then, it would make sense that the App only shows
female dogs to him, right? We can easily achieve this using queries:

```javascript
const dogo_profile = gql`
    query GetDogoProfile {
        dogos(sex: "female") {
            name, 
            age,
            sex,
            breed,
            profileDescription,
            selfies {
                url
            }
        }
    }
`;
```

That is the **same** query from above but we filter `dogos` by `sex` so that
only female dogos are shown to him. This is done on the backend once we request
it so that we dont overfetch! How about only female dogos between 6 and 8 years
of age?

```javascript
const dogo_profile = gql`
    query GetDogoProfile {
        dogos(sex: "female", age: [6,7,8]) {
            name, 
            age,
            sex,
            breed,
            profileDescription,
            selfies {
                url
            }
        }
    }
`;
```

GraphQL is really powerfull, especially with the well documented tools that help
you write these queries as well as implement the backend and types. So, dont
worry if these queries look intimidating to write. There are tools that will
help you with it and they make it extremely hard to break things.

Back to the main page!