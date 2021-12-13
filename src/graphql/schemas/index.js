const { gql } = require('apollo-server-express');
const patientType = require('./patient')
const studyType = require('./study')
const seriesType = require('./series')
const fileType = require('./file')
const modalityType = require('./modality')

const rootType = gql`
 type Query {
     root: String
 }
 type Mutation {
     root: String
 }

`;

module.exports = [rootType, patientType, studyType, seriesType, fileType, modalityType];