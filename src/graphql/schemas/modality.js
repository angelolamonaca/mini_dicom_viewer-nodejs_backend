const {gql} = require('apollo-server-express');

module.exports = gql`

 type Modality {
     id: Int!
     name: String!
     series: [Series!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllModalities: [Modality!]
    getSingleModality(id: Int!): Modality
}

 extend type Mutation {
     createModality(name: String!): CreateModalityResponse
     deleteModality(id: Int!): Int
 }

 type CreateModalityResponse {
    id: Int!
    name: String!
    createdAt: String!
 }

`;