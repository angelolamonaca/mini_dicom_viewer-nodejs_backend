const {gql} = require('apollo-server-express');

module.exports = gql`

 type Study {
     idStudy: Int!
     studyName: String!
     patient: Patient!
     series: [Series!]
     files: [File!]
     createdAt: String
     updatedAt: String
 }

extend type Query {
    getAllStudies: [Study!]
    getSingleStudy(idStudy: Int!): Study
}

 extend type Mutation {
     createStudy(studyName: String!): CreateStudyResponse
 }

 type CreateStudyResponse {
    idStudy: Int!
    studyName: String!
    createdAt: String!
 }

`;