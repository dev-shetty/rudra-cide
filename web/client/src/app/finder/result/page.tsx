type FinderSearchParams = {
  username: string
  key: string
}

async function getUserAlias(username: string, key: string) {
  const body = {
    username,
    key,
  }

  const response = await fetch(
    `${process.env.NEXT_PUBLIC_BACKEND_BASE_URL}/api/v1/alias/alias-user`,
    {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    }
  )
  const data = await response.json()
  return data
}

export default async function FinderResult({
  params,
}: {
  params: FinderSearchParams
}) {
  const { username, key } = params
  const userAlias = await getUserAlias(username, key)
  console.log(userAlias)

  return (
    <div>
      <h1>Hello</h1>
    </div>
  )
}
