const {gql} = require('apollo-server-express');

module.exports = gql`

 type Study {
     id: Int!
     studyName: String!
     idPatient: Int!
     series: [Series!]
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllStudies: [Study!]
    getSingleStudy(id: Int!): Study
}

 extend type Mutation {
     createStudy(studyName: String!, idPatient: Int!): CreateStudyResponse
 }

 type CreateStudyResponse {
    id: Int!
    studyName: String!
    idPatient: Int!
    createdAt: String!
 }

`;