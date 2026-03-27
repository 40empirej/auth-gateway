const { parse } = require('graphql');

const parseQuery = (query) => {
  try {
    const result = parse(query);
    return result;
  } catch (error) {
    return { errors: [error.message] };
  }
};

module.exports = { parseQuery };