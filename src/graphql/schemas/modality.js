const {gql} = require('apollo-server-express');

module.exports = gql`

 type Modality {
     idModality: Int!
     name: String!
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllModalities: [Modality!]
    getSingleModality(idModality: Int!): Modality
}

 extend type Mutation {
     createModality(name: String!): CreateModalityResponse
 }

 type CreateModalityResponse {
    idModality: Int!
    name: String!
    createdAt: String!
 }

`;