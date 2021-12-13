const {gql} = require('apollo-server-express');

module.exports = gql`

 type Patient {
     idPatient: Int!
     name: String!
     studies: [Study!]
     series: [Series!]
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllPatients: [Patient!]
    getSinglePatient(idPatient: Int!): Patient
}

 extend type Mutation {
     createPatient(name: String!): CreatePatientResponse
 }

 type CreatePatientResponse {
    idPatient: Int!
    name: String!
    createdAt: String!
 }

`;