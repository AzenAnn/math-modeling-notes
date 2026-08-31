function [closeness, ranking] = implementation(matrix, weights, benefit)
% TOPSIS reusable implementation.
% Source evidence: E-TEXT-P002-TOPSIS-DEMO
% Generic validation is EXTERNAL_REFERENCE.

if nargin < 3
    benefit = true(1, size(matrix, 2));
end
if isempty(matrix) || ndims(matrix) ~= 2
    error('matrix must be a non-empty 2D array');
end
weights = weights(:)';
benefit = logical(benefit(:)');
if length(weights) ~= size(matrix, 2) || length(benefit) ~= size(matrix, 2)
    error('weights and benefit must match the number of indicators');
end
if any(weights < 0) || sum(weights) <= 0
    error('weights must be nonnegative and have a positive sum');
end
norms = sqrt(sum(matrix .^ 2, 1));
if any(norms == 0)
    error('an indicator column has zero vector norm');
end
normalized = matrix ./ norms;
weighted = normalized .* (weights / sum(weights));
positive = max(weighted, [], 1);
negative = min(weighted, [], 1);
positive(~benefit) = min(weighted(:, ~benefit), [], 1);
negative(~benefit) = max(weighted(:, ~benefit), [], 1);
dPositive = sqrt(sum((weighted - positive) .^ 2, 2));
dNegative = sqrt(sum((weighted - negative) .^ 2, 2));
denominator = dPositive + dNegative;
closeness = 0.5 * ones(size(denominator));
mask = denominator > 0;
closeness(mask) = dNegative(mask) ./ denominator(mask);
[~, ranking] = sort(closeness, 'descend');
end
