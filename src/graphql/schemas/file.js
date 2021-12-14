const {gql} = require('apollo-server-express');

module.exports = gql`

 type File {
     id: Int!
     filePath: String!
     idPatient: Int!
     idStudy: Int!
     idSeries: Int!
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllFiles: [File!]
    getSingleFile(id: Int!, idPatient: Int!, idStudy: Int!, idSeries: Int!): File
}

 extend type Mutation {
     createFile(filePath: String!, idPatient: Int!, idStudy: Int!, idSeries: Int!): CreateFileResponse
 }

 type CreateFileResponse {
    id: Int!
    filePath: String!
    idPatient: Int!
    idStudy: Int!
    idSeries: Int!
    createdAt: String!
 }

`;