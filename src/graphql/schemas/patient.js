const {gql} = require('apollo-server-express');

module.exports = gql`

 type Patient {
     id: Int!
     name: String!
     studies: [Study!]
     series: [Series!]
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllPatients: [Patient!]
    getSinglePatient(id: Int!): Patient
}

 extend type Mutation {
     createPatient(name: String!): CreatePatientResponse
 }

 type CreatePatientResponse {
    id: Int!
    name: String!
    createdAt: String!
 }

`;