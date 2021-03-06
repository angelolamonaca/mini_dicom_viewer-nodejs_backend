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
    getSingleFile(id: Int!): File
}

 extend type Mutation {
     createFile(filePath: String!, idPatient: Int!, idStudy: Int!, idSeries: Int!): CreateFileResponse
     editFile(id: Int!, filePath: String!): [Int]
     deleteFile(id: Int!): Int
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