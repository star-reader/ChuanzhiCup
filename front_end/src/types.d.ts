type UserInfo = {
    id: number,
    username: string,
    avatar: string,
    email: string,
    bio: string,
    token: string
}

type SupplierInfo = UserInfo& {
    authorizationCode: string,
}


type Items = {
    id: number,
    name: string,
    tags: string, // 字符串存，用,或，分割，前端split后展示
    price: number,
    description: string,
    image: string,
    createdAt: string,
    fresh_level: string | number,
    period: string,
    ranking: number
}
