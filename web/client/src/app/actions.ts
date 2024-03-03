import { createClient } from "redis"

export async function redisClient() {
  const client = await createClient()
    .on("error", (err) => console.log(err))
    .connect()

  return client
}
