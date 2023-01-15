# Combining Data fetching and Displaying

This will probably the last theory section. We will finally make use of our
knowledge to connect data to the rendering process! I will reuse the Tinder for
dogos example from last chapter (Check it out [here](./fetching.md)).

## Requesting

In the last chapter, I talked a lot queries. Well, these queries actually to not
get the data! You have to request it using the query to get your data. It's like
fishing: Your bait cannot fish, only you can fish using the bait. In React, we
can use the `useQuery` Hook to request data. Yes, this hook is very similar to
the `useState` hook. However, instead of manually initializing a value, the hook
will ask the backend to give the state a value!

```javascript
// taken from Chapter about data fetching
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

function Dogs() {
  // this executes the query and load the data into the variables
  const { loading, error, data } = useQuery(dogo_profile);

  // conditional rendering: You should know that :)
  if (loading) // as long as we laod the data, show "Loading..." 
    return (<div>Loading...</div>)

  if (error) // if an error happen, we want to show "Error! .." 
    return (<div>Error! {error.message}</div>)

  // Data has loaded successfully!
  // we could inject even fields such as e.g. data.dogos.sex etc. 
  return (
    <div>
        <img src={data.dogos.selfies[0].url}>
        <h1> {data.dogos.name} </h1>
    </div>
  );
}
```

Assuming the `useQuery` will return data looking like this:

```json
{
    "dogos": {
            "name": "Lili",
            "age": 6,
            "sex": "female",
            "breed": "Golden Retriever",
            "profileDescription": "You can chase my tail ;)",
            "selfies": [
                {
                    "url" : "https://tinder4dogos.com/pb/lili_pic_1.jpg",
                },
                {
                    "url" : "https://tinder4dogos.com/pb/lili_pic_2.jpg",
                },
            ]
    }
}
```

I think you should be able to get this one. We used `useQuery` to load the data
from the server and destruct it into the variables `loading`, `error`, `data`.
We used conditional Rendering to show the status. Note that for the `src`
property of the image, we had to use `data.dogos.selfies[0].url`. If you look in
to the data of that `useQuery`, this should make sense (*try to follow the path
from 'dogos' to 'url'*).

That's about the basics! Everything else, you should learn from documentations
as it is impossible to cover everything.